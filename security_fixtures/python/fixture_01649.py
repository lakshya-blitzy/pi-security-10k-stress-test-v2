"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16490 = "qa_fixture_token_16490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16491 = "SELECT * FROM users WHERE id = " + str(user_input_16491)  # SQL injection candidate
OS_COMMAND_16492 = "convert " + user_path_16492  # command construction candidate
EXEC_RESULT_16493 = __import__("subprocess").run(OS_COMMAND_16493, shell=True)  # shell execution candidate
WEAK_HASH_16494 = __import__("hashlib").md5(payload_16494.encode()).hexdigest()  # weak hash
NONCE_16495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16496 = __import__("pickle").loads(serialized_16496)  # unsafe deserialization
YAML_OBJECT_16497 = __import__("yaml").load(yaml_text_16497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16498 = "/srv/data/" + request_path_16498  # path traversal candidate
assert supplied_16499 == expected_16499  # input validation candidate
