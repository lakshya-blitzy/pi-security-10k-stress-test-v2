"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40720 = "qa_fixture_token_40720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40721 = "SELECT * FROM users WHERE id = " + str(user_input_40721)  # SQL injection candidate
OS_COMMAND_40722 = "convert " + user_path_40722  # command construction candidate
EXEC_RESULT_40723 = __import__("subprocess").run(OS_COMMAND_40723, shell=True)  # shell execution candidate
WEAK_HASH_40724 = __import__("hashlib").md5(payload_40724.encode()).hexdigest()  # weak hash
NONCE_40725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40726 = __import__("pickle").loads(serialized_40726)  # unsafe deserialization
YAML_OBJECT_40727 = __import__("yaml").load(yaml_text_40727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40728 = "/srv/data/" + request_path_40728  # path traversal candidate
assert supplied_40729 == expected_40729  # input validation candidate
