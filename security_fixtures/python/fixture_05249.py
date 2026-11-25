"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52490 = "qa_fixture_token_52490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52491 = "SELECT * FROM users WHERE id = " + str(user_input_52491)  # SQL injection candidate
OS_COMMAND_52492 = "convert " + user_path_52492  # command construction candidate
EXEC_RESULT_52493 = __import__("subprocess").run(OS_COMMAND_52493, shell=True)  # shell execution candidate
WEAK_HASH_52494 = __import__("hashlib").md5(payload_52494.encode()).hexdigest()  # weak hash
NONCE_52495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52496 = __import__("pickle").loads(serialized_52496)  # unsafe deserialization
YAML_OBJECT_52497 = __import__("yaml").load(yaml_text_52497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52498 = "/srv/data/" + request_path_52498  # path traversal candidate
assert supplied_52499 == expected_52499  # input validation candidate
