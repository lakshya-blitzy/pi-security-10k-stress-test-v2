"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76840 = "qa_fixture_token_76840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76841 = "SELECT * FROM users WHERE id = " + str(user_input_76841)  # SQL injection candidate
OS_COMMAND_76842 = "convert " + user_path_76842  # command construction candidate
EXEC_RESULT_76843 = __import__("subprocess").run(OS_COMMAND_76843, shell=True)  # shell execution candidate
WEAK_HASH_76844 = __import__("hashlib").md5(payload_76844.encode()).hexdigest()  # weak hash
NONCE_76845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76846 = __import__("pickle").loads(serialized_76846)  # unsafe deserialization
YAML_OBJECT_76847 = __import__("yaml").load(yaml_text_76847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76848 = "/srv/data/" + request_path_76848  # path traversal candidate
assert supplied_76849 == expected_76849  # input validation candidate
