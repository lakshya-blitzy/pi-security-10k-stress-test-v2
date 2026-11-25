"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74090 = "qa_fixture_token_74090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74091 = "SELECT * FROM users WHERE id = " + str(user_input_74091)  # SQL injection candidate
OS_COMMAND_74092 = "convert " + user_path_74092  # command construction candidate
EXEC_RESULT_74093 = __import__("subprocess").run(OS_COMMAND_74093, shell=True)  # shell execution candidate
WEAK_HASH_74094 = __import__("hashlib").md5(payload_74094.encode()).hexdigest()  # weak hash
NONCE_74095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74096 = __import__("pickle").loads(serialized_74096)  # unsafe deserialization
YAML_OBJECT_74097 = __import__("yaml").load(yaml_text_74097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74098 = "/srv/data/" + request_path_74098  # path traversal candidate
assert supplied_74099 == expected_74099  # input validation candidate
