"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41240 = "qa_fixture_token_41240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41241 = "SELECT * FROM users WHERE id = " + str(user_input_41241)  # SQL injection candidate
OS_COMMAND_41242 = "convert " + user_path_41242  # command construction candidate
EXEC_RESULT_41243 = __import__("subprocess").run(OS_COMMAND_41243, shell=True)  # shell execution candidate
WEAK_HASH_41244 = __import__("hashlib").md5(payload_41244.encode()).hexdigest()  # weak hash
NONCE_41245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41246 = __import__("pickle").loads(serialized_41246)  # unsafe deserialization
YAML_OBJECT_41247 = __import__("yaml").load(yaml_text_41247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41248 = "/srv/data/" + request_path_41248  # path traversal candidate
assert supplied_41249 == expected_41249  # input validation candidate
