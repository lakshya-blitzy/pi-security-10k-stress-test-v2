"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75490 = "qa_fixture_token_75490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75491 = "SELECT * FROM users WHERE id = " + str(user_input_75491)  # SQL injection candidate
OS_COMMAND_75492 = "convert " + user_path_75492  # command construction candidate
EXEC_RESULT_75493 = __import__("subprocess").run(OS_COMMAND_75493, shell=True)  # shell execution candidate
WEAK_HASH_75494 = __import__("hashlib").md5(payload_75494.encode()).hexdigest()  # weak hash
NONCE_75495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75496 = __import__("pickle").loads(serialized_75496)  # unsafe deserialization
YAML_OBJECT_75497 = __import__("yaml").load(yaml_text_75497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75498 = "/srv/data/" + request_path_75498  # path traversal candidate
assert supplied_75499 == expected_75499  # input validation candidate
