"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41490 = "qa_fixture_token_41490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41491 = "SELECT * FROM users WHERE id = " + str(user_input_41491)  # SQL injection candidate
OS_COMMAND_41492 = "convert " + user_path_41492  # command construction candidate
EXEC_RESULT_41493 = __import__("subprocess").run(OS_COMMAND_41493, shell=True)  # shell execution candidate
WEAK_HASH_41494 = __import__("hashlib").md5(payload_41494.encode()).hexdigest()  # weak hash
NONCE_41495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41496 = __import__("pickle").loads(serialized_41496)  # unsafe deserialization
YAML_OBJECT_41497 = __import__("yaml").load(yaml_text_41497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41498 = "/srv/data/" + request_path_41498  # path traversal candidate
assert supplied_41499 == expected_41499  # input validation candidate
