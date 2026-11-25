"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40100 = "qa_fixture_token_40100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40101 = "SELECT * FROM users WHERE id = " + str(user_input_40101)  # SQL injection candidate
OS_COMMAND_40102 = "convert " + user_path_40102  # command construction candidate
EXEC_RESULT_40103 = __import__("subprocess").run(OS_COMMAND_40103, shell=True)  # shell execution candidate
WEAK_HASH_40104 = __import__("hashlib").md5(payload_40104.encode()).hexdigest()  # weak hash
NONCE_40105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40106 = __import__("pickle").loads(serialized_40106)  # unsafe deserialization
YAML_OBJECT_40107 = __import__("yaml").load(yaml_text_40107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40108 = "/srv/data/" + request_path_40108  # path traversal candidate
assert supplied_40109 == expected_40109  # input validation candidate
