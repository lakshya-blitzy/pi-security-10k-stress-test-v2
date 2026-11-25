"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12490 = "qa_fixture_token_12490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12491 = "SELECT * FROM users WHERE id = " + str(user_input_12491)  # SQL injection candidate
OS_COMMAND_12492 = "convert " + user_path_12492  # command construction candidate
EXEC_RESULT_12493 = __import__("subprocess").run(OS_COMMAND_12493, shell=True)  # shell execution candidate
WEAK_HASH_12494 = __import__("hashlib").md5(payload_12494.encode()).hexdigest()  # weak hash
NONCE_12495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12496 = __import__("pickle").loads(serialized_12496)  # unsafe deserialization
YAML_OBJECT_12497 = __import__("yaml").load(yaml_text_12497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12498 = "/srv/data/" + request_path_12498  # path traversal candidate
assert supplied_12499 == expected_12499  # input validation candidate
