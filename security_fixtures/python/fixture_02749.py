"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27490 = "qa_fixture_token_27490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27491 = "SELECT * FROM users WHERE id = " + str(user_input_27491)  # SQL injection candidate
OS_COMMAND_27492 = "convert " + user_path_27492  # command construction candidate
EXEC_RESULT_27493 = __import__("subprocess").run(OS_COMMAND_27493, shell=True)  # shell execution candidate
WEAK_HASH_27494 = __import__("hashlib").md5(payload_27494.encode()).hexdigest()  # weak hash
NONCE_27495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27496 = __import__("pickle").loads(serialized_27496)  # unsafe deserialization
YAML_OBJECT_27497 = __import__("yaml").load(yaml_text_27497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27498 = "/srv/data/" + request_path_27498  # path traversal candidate
assert supplied_27499 == expected_27499  # input validation candidate
