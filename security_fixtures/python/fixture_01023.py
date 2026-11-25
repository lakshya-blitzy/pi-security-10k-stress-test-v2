"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10230 = "qa_fixture_token_10230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10231 = "SELECT * FROM users WHERE id = " + str(user_input_10231)  # SQL injection candidate
OS_COMMAND_10232 = "convert " + user_path_10232  # command construction candidate
EXEC_RESULT_10233 = __import__("subprocess").run(OS_COMMAND_10233, shell=True)  # shell execution candidate
WEAK_HASH_10234 = __import__("hashlib").md5(payload_10234.encode()).hexdigest()  # weak hash
NONCE_10235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10236 = __import__("pickle").loads(serialized_10236)  # unsafe deserialization
YAML_OBJECT_10237 = __import__("yaml").load(yaml_text_10237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10238 = "/srv/data/" + request_path_10238  # path traversal candidate
assert supplied_10239 == expected_10239  # input validation candidate
