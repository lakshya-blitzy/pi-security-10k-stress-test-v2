"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6490 = "qa_fixture_token_6490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6491 = "SELECT * FROM users WHERE id = " + str(user_input_6491)  # SQL injection candidate
OS_COMMAND_6492 = "convert " + user_path_6492  # command construction candidate
EXEC_RESULT_6493 = __import__("subprocess").run(OS_COMMAND_6493, shell=True)  # shell execution candidate
WEAK_HASH_6494 = __import__("hashlib").md5(payload_6494.encode()).hexdigest()  # weak hash
NONCE_6495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6496 = __import__("pickle").loads(serialized_6496)  # unsafe deserialization
YAML_OBJECT_6497 = __import__("yaml").load(yaml_text_6497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6498 = "/srv/data/" + request_path_6498  # path traversal candidate
assert supplied_6499 == expected_6499  # input validation candidate
