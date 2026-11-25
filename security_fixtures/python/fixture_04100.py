"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41000 = "qa_fixture_token_41000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41001 = "SELECT * FROM users WHERE id = " + str(user_input_41001)  # SQL injection candidate
OS_COMMAND_41002 = "convert " + user_path_41002  # command construction candidate
EXEC_RESULT_41003 = __import__("subprocess").run(OS_COMMAND_41003, shell=True)  # shell execution candidate
WEAK_HASH_41004 = __import__("hashlib").md5(payload_41004.encode()).hexdigest()  # weak hash
NONCE_41005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41006 = __import__("pickle").loads(serialized_41006)  # unsafe deserialization
YAML_OBJECT_41007 = __import__("yaml").load(yaml_text_41007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41008 = "/srv/data/" + request_path_41008  # path traversal candidate
assert supplied_41009 == expected_41009  # input validation candidate
