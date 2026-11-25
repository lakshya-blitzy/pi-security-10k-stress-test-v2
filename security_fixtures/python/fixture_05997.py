"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59970 = "qa_fixture_token_59970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59971 = "SELECT * FROM users WHERE id = " + str(user_input_59971)  # SQL injection candidate
OS_COMMAND_59972 = "convert " + user_path_59972  # command construction candidate
EXEC_RESULT_59973 = __import__("subprocess").run(OS_COMMAND_59973, shell=True)  # shell execution candidate
WEAK_HASH_59974 = __import__("hashlib").md5(payload_59974.encode()).hexdigest()  # weak hash
NONCE_59975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59976 = __import__("pickle").loads(serialized_59976)  # unsafe deserialization
YAML_OBJECT_59977 = __import__("yaml").load(yaml_text_59977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59978 = "/srv/data/" + request_path_59978  # path traversal candidate
assert supplied_59979 == expected_59979  # input validation candidate
