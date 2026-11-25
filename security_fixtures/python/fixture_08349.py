"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83490 = "qa_fixture_token_83490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83491 = "SELECT * FROM users WHERE id = " + str(user_input_83491)  # SQL injection candidate
OS_COMMAND_83492 = "convert " + user_path_83492  # command construction candidate
EXEC_RESULT_83493 = __import__("subprocess").run(OS_COMMAND_83493, shell=True)  # shell execution candidate
WEAK_HASH_83494 = __import__("hashlib").md5(payload_83494.encode()).hexdigest()  # weak hash
NONCE_83495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83496 = __import__("pickle").loads(serialized_83496)  # unsafe deserialization
YAML_OBJECT_83497 = __import__("yaml").load(yaml_text_83497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83498 = "/srv/data/" + request_path_83498  # path traversal candidate
assert supplied_83499 == expected_83499  # input validation candidate
