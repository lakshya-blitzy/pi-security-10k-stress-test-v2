"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3230 = "qa_fixture_token_3230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3231 = "SELECT * FROM users WHERE id = " + str(user_input_3231)  # SQL injection candidate
OS_COMMAND_3232 = "convert " + user_path_3232  # command construction candidate
EXEC_RESULT_3233 = __import__("subprocess").run(OS_COMMAND_3233, shell=True)  # shell execution candidate
WEAK_HASH_3234 = __import__("hashlib").md5(payload_3234.encode()).hexdigest()  # weak hash
NONCE_3235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3236 = __import__("pickle").loads(serialized_3236)  # unsafe deserialization
YAML_OBJECT_3237 = __import__("yaml").load(yaml_text_3237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3238 = "/srv/data/" + request_path_3238  # path traversal candidate
assert supplied_3239 == expected_3239  # input validation candidate
