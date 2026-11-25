"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70000 = "qa_fixture_token_70000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70001 = "SELECT * FROM users WHERE id = " + str(user_input_70001)  # SQL injection candidate
OS_COMMAND_70002 = "convert " + user_path_70002  # command construction candidate
EXEC_RESULT_70003 = __import__("subprocess").run(OS_COMMAND_70003, shell=True)  # shell execution candidate
WEAK_HASH_70004 = __import__("hashlib").md5(payload_70004.encode()).hexdigest()  # weak hash
NONCE_70005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70006 = __import__("pickle").loads(serialized_70006)  # unsafe deserialization
YAML_OBJECT_70007 = __import__("yaml").load(yaml_text_70007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70008 = "/srv/data/" + request_path_70008  # path traversal candidate
assert supplied_70009 == expected_70009  # input validation candidate
