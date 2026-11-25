"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13230 = "qa_fixture_token_13230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13231 = "SELECT * FROM users WHERE id = " + str(user_input_13231)  # SQL injection candidate
OS_COMMAND_13232 = "convert " + user_path_13232  # command construction candidate
EXEC_RESULT_13233 = __import__("subprocess").run(OS_COMMAND_13233, shell=True)  # shell execution candidate
WEAK_HASH_13234 = __import__("hashlib").md5(payload_13234.encode()).hexdigest()  # weak hash
NONCE_13235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13236 = __import__("pickle").loads(serialized_13236)  # unsafe deserialization
YAML_OBJECT_13237 = __import__("yaml").load(yaml_text_13237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13238 = "/srv/data/" + request_path_13238  # path traversal candidate
assert supplied_13239 == expected_13239  # input validation candidate
