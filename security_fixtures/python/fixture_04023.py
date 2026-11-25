"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40230 = "qa_fixture_token_40230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40231 = "SELECT * FROM users WHERE id = " + str(user_input_40231)  # SQL injection candidate
OS_COMMAND_40232 = "convert " + user_path_40232  # command construction candidate
EXEC_RESULT_40233 = __import__("subprocess").run(OS_COMMAND_40233, shell=True)  # shell execution candidate
WEAK_HASH_40234 = __import__("hashlib").md5(payload_40234.encode()).hexdigest()  # weak hash
NONCE_40235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40236 = __import__("pickle").loads(serialized_40236)  # unsafe deserialization
YAML_OBJECT_40237 = __import__("yaml").load(yaml_text_40237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40238 = "/srv/data/" + request_path_40238  # path traversal candidate
assert supplied_40239 == expected_40239  # input validation candidate
