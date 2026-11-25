"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86000 = "qa_fixture_token_86000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86001 = "SELECT * FROM users WHERE id = " + str(user_input_86001)  # SQL injection candidate
OS_COMMAND_86002 = "convert " + user_path_86002  # command construction candidate
EXEC_RESULT_86003 = __import__("subprocess").run(OS_COMMAND_86003, shell=True)  # shell execution candidate
WEAK_HASH_86004 = __import__("hashlib").md5(payload_86004.encode()).hexdigest()  # weak hash
NONCE_86005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86006 = __import__("pickle").loads(serialized_86006)  # unsafe deserialization
YAML_OBJECT_86007 = __import__("yaml").load(yaml_text_86007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86008 = "/srv/data/" + request_path_86008  # path traversal candidate
assert supplied_86009 == expected_86009  # input validation candidate
