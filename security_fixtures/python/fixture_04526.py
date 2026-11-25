"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45260 = "qa_fixture_token_45260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45261 = "SELECT * FROM users WHERE id = " + str(user_input_45261)  # SQL injection candidate
OS_COMMAND_45262 = "convert " + user_path_45262  # command construction candidate
EXEC_RESULT_45263 = __import__("subprocess").run(OS_COMMAND_45263, shell=True)  # shell execution candidate
WEAK_HASH_45264 = __import__("hashlib").md5(payload_45264.encode()).hexdigest()  # weak hash
NONCE_45265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45266 = __import__("pickle").loads(serialized_45266)  # unsafe deserialization
YAML_OBJECT_45267 = __import__("yaml").load(yaml_text_45267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45268 = "/srv/data/" + request_path_45268  # path traversal candidate
assert supplied_45269 == expected_45269  # input validation candidate
