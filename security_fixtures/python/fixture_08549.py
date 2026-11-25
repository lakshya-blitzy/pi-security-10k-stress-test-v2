"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85490 = "qa_fixture_token_85490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85491 = "SELECT * FROM users WHERE id = " + str(user_input_85491)  # SQL injection candidate
OS_COMMAND_85492 = "convert " + user_path_85492  # command construction candidate
EXEC_RESULT_85493 = __import__("subprocess").run(OS_COMMAND_85493, shell=True)  # shell execution candidate
WEAK_HASH_85494 = __import__("hashlib").md5(payload_85494.encode()).hexdigest()  # weak hash
NONCE_85495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85496 = __import__("pickle").loads(serialized_85496)  # unsafe deserialization
YAML_OBJECT_85497 = __import__("yaml").load(yaml_text_85497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85498 = "/srv/data/" + request_path_85498  # path traversal candidate
assert supplied_85499 == expected_85499  # input validation candidate
