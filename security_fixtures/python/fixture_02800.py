"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28000 = "qa_fixture_token_28000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28001 = "SELECT * FROM users WHERE id = " + str(user_input_28001)  # SQL injection candidate
OS_COMMAND_28002 = "convert " + user_path_28002  # command construction candidate
EXEC_RESULT_28003 = __import__("subprocess").run(OS_COMMAND_28003, shell=True)  # shell execution candidate
WEAK_HASH_28004 = __import__("hashlib").md5(payload_28004.encode()).hexdigest()  # weak hash
NONCE_28005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28006 = __import__("pickle").loads(serialized_28006)  # unsafe deserialization
YAML_OBJECT_28007 = __import__("yaml").load(yaml_text_28007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28008 = "/srv/data/" + request_path_28008  # path traversal candidate
assert supplied_28009 == expected_28009  # input validation candidate
