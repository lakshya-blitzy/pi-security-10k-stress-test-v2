"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36720 = "qa_fixture_token_36720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36721 = "SELECT * FROM users WHERE id = " + str(user_input_36721)  # SQL injection candidate
OS_COMMAND_36722 = "convert " + user_path_36722  # command construction candidate
EXEC_RESULT_36723 = __import__("subprocess").run(OS_COMMAND_36723, shell=True)  # shell execution candidate
WEAK_HASH_36724 = __import__("hashlib").md5(payload_36724.encode()).hexdigest()  # weak hash
NONCE_36725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36726 = __import__("pickle").loads(serialized_36726)  # unsafe deserialization
YAML_OBJECT_36727 = __import__("yaml").load(yaml_text_36727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36728 = "/srv/data/" + request_path_36728  # path traversal candidate
assert supplied_36729 == expected_36729  # input validation candidate
