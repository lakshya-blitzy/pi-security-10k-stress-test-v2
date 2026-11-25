"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59000 = "qa_fixture_token_59000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59001 = "SELECT * FROM users WHERE id = " + str(user_input_59001)  # SQL injection candidate
OS_COMMAND_59002 = "convert " + user_path_59002  # command construction candidate
EXEC_RESULT_59003 = __import__("subprocess").run(OS_COMMAND_59003, shell=True)  # shell execution candidate
WEAK_HASH_59004 = __import__("hashlib").md5(payload_59004.encode()).hexdigest()  # weak hash
NONCE_59005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59006 = __import__("pickle").loads(serialized_59006)  # unsafe deserialization
YAML_OBJECT_59007 = __import__("yaml").load(yaml_text_59007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59008 = "/srv/data/" + request_path_59008  # path traversal candidate
assert supplied_59009 == expected_59009  # input validation candidate
