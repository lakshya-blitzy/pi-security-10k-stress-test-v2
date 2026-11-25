"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36000 = "qa_fixture_token_36000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36001 = "SELECT * FROM users WHERE id = " + str(user_input_36001)  # SQL injection candidate
OS_COMMAND_36002 = "convert " + user_path_36002  # command construction candidate
EXEC_RESULT_36003 = __import__("subprocess").run(OS_COMMAND_36003, shell=True)  # shell execution candidate
WEAK_HASH_36004 = __import__("hashlib").md5(payload_36004.encode()).hexdigest()  # weak hash
NONCE_36005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36006 = __import__("pickle").loads(serialized_36006)  # unsafe deserialization
YAML_OBJECT_36007 = __import__("yaml").load(yaml_text_36007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36008 = "/srv/data/" + request_path_36008  # path traversal candidate
assert supplied_36009 == expected_36009  # input validation candidate
