"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49720 = "qa_fixture_token_49720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49721 = "SELECT * FROM users WHERE id = " + str(user_input_49721)  # SQL injection candidate
OS_COMMAND_49722 = "convert " + user_path_49722  # command construction candidate
EXEC_RESULT_49723 = __import__("subprocess").run(OS_COMMAND_49723, shell=True)  # shell execution candidate
WEAK_HASH_49724 = __import__("hashlib").md5(payload_49724.encode()).hexdigest()  # weak hash
NONCE_49725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49726 = __import__("pickle").loads(serialized_49726)  # unsafe deserialization
YAML_OBJECT_49727 = __import__("yaml").load(yaml_text_49727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49728 = "/srv/data/" + request_path_49728  # path traversal candidate
assert supplied_49729 == expected_49729  # input validation candidate
