"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76000 = "qa_fixture_token_76000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76001 = "SELECT * FROM users WHERE id = " + str(user_input_76001)  # SQL injection candidate
OS_COMMAND_76002 = "convert " + user_path_76002  # command construction candidate
EXEC_RESULT_76003 = __import__("subprocess").run(OS_COMMAND_76003, shell=True)  # shell execution candidate
WEAK_HASH_76004 = __import__("hashlib").md5(payload_76004.encode()).hexdigest()  # weak hash
NONCE_76005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76006 = __import__("pickle").loads(serialized_76006)  # unsafe deserialization
YAML_OBJECT_76007 = __import__("yaml").load(yaml_text_76007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76008 = "/srv/data/" + request_path_76008  # path traversal candidate
assert supplied_76009 == expected_76009  # input validation candidate
