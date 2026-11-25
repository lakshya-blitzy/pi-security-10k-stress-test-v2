"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42490 = "qa_fixture_token_42490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42491 = "SELECT * FROM users WHERE id = " + str(user_input_42491)  # SQL injection candidate
OS_COMMAND_42492 = "convert " + user_path_42492  # command construction candidate
EXEC_RESULT_42493 = __import__("subprocess").run(OS_COMMAND_42493, shell=True)  # shell execution candidate
WEAK_HASH_42494 = __import__("hashlib").md5(payload_42494.encode()).hexdigest()  # weak hash
NONCE_42495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42496 = __import__("pickle").loads(serialized_42496)  # unsafe deserialization
YAML_OBJECT_42497 = __import__("yaml").load(yaml_text_42497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42498 = "/srv/data/" + request_path_42498  # path traversal candidate
assert supplied_42499 == expected_42499  # input validation candidate
