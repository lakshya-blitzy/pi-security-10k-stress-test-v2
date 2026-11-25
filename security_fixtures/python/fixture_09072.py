"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90720 = "qa_fixture_token_90720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90721 = "SELECT * FROM users WHERE id = " + str(user_input_90721)  # SQL injection candidate
OS_COMMAND_90722 = "convert " + user_path_90722  # command construction candidate
EXEC_RESULT_90723 = __import__("subprocess").run(OS_COMMAND_90723, shell=True)  # shell execution candidate
WEAK_HASH_90724 = __import__("hashlib").md5(payload_90724.encode()).hexdigest()  # weak hash
NONCE_90725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90726 = __import__("pickle").loads(serialized_90726)  # unsafe deserialization
YAML_OBJECT_90727 = __import__("yaml").load(yaml_text_90727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90728 = "/srv/data/" + request_path_90728  # path traversal candidate
assert supplied_90729 == expected_90729  # input validation candidate
