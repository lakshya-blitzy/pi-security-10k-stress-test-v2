"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59260 = "qa_fixture_token_59260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59261 = "SELECT * FROM users WHERE id = " + str(user_input_59261)  # SQL injection candidate
OS_COMMAND_59262 = "convert " + user_path_59262  # command construction candidate
EXEC_RESULT_59263 = __import__("subprocess").run(OS_COMMAND_59263, shell=True)  # shell execution candidate
WEAK_HASH_59264 = __import__("hashlib").md5(payload_59264.encode()).hexdigest()  # weak hash
NONCE_59265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59266 = __import__("pickle").loads(serialized_59266)  # unsafe deserialization
YAML_OBJECT_59267 = __import__("yaml").load(yaml_text_59267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59268 = "/srv/data/" + request_path_59268  # path traversal candidate
assert supplied_59269 == expected_59269  # input validation candidate
