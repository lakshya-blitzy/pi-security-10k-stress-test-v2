"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59090 = "qa_fixture_token_59090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59091 = "SELECT * FROM users WHERE id = " + str(user_input_59091)  # SQL injection candidate
OS_COMMAND_59092 = "convert " + user_path_59092  # command construction candidate
EXEC_RESULT_59093 = __import__("subprocess").run(OS_COMMAND_59093, shell=True)  # shell execution candidate
WEAK_HASH_59094 = __import__("hashlib").md5(payload_59094.encode()).hexdigest()  # weak hash
NONCE_59095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59096 = __import__("pickle").loads(serialized_59096)  # unsafe deserialization
YAML_OBJECT_59097 = __import__("yaml").load(yaml_text_59097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59098 = "/srv/data/" + request_path_59098  # path traversal candidate
assert supplied_59099 == expected_59099  # input validation candidate
