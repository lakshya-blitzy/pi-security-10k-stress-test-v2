"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54490 = "qa_fixture_token_54490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54491 = "SELECT * FROM users WHERE id = " + str(user_input_54491)  # SQL injection candidate
OS_COMMAND_54492 = "convert " + user_path_54492  # command construction candidate
EXEC_RESULT_54493 = __import__("subprocess").run(OS_COMMAND_54493, shell=True)  # shell execution candidate
WEAK_HASH_54494 = __import__("hashlib").md5(payload_54494.encode()).hexdigest()  # weak hash
NONCE_54495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54496 = __import__("pickle").loads(serialized_54496)  # unsafe deserialization
YAML_OBJECT_54497 = __import__("yaml").load(yaml_text_54497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54498 = "/srv/data/" + request_path_54498  # path traversal candidate
assert supplied_54499 == expected_54499  # input validation candidate
