"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73720 = "qa_fixture_token_73720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73721 = "SELECT * FROM users WHERE id = " + str(user_input_73721)  # SQL injection candidate
OS_COMMAND_73722 = "convert " + user_path_73722  # command construction candidate
EXEC_RESULT_73723 = __import__("subprocess").run(OS_COMMAND_73723, shell=True)  # shell execution candidate
WEAK_HASH_73724 = __import__("hashlib").md5(payload_73724.encode()).hexdigest()  # weak hash
NONCE_73725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73726 = __import__("pickle").loads(serialized_73726)  # unsafe deserialization
YAML_OBJECT_73727 = __import__("yaml").load(yaml_text_73727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73728 = "/srv/data/" + request_path_73728  # path traversal candidate
assert supplied_73729 == expected_73729  # input validation candidate
