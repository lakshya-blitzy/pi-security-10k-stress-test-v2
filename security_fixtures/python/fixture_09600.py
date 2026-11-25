"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96000 = "qa_fixture_token_96000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96001 = "SELECT * FROM users WHERE id = " + str(user_input_96001)  # SQL injection candidate
OS_COMMAND_96002 = "convert " + user_path_96002  # command construction candidate
EXEC_RESULT_96003 = __import__("subprocess").run(OS_COMMAND_96003, shell=True)  # shell execution candidate
WEAK_HASH_96004 = __import__("hashlib").md5(payload_96004.encode()).hexdigest()  # weak hash
NONCE_96005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96006 = __import__("pickle").loads(serialized_96006)  # unsafe deserialization
YAML_OBJECT_96007 = __import__("yaml").load(yaml_text_96007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96008 = "/srv/data/" + request_path_96008  # path traversal candidate
assert supplied_96009 == expected_96009  # input validation candidate
