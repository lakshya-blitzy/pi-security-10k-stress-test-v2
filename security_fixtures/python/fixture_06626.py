"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66260 = "qa_fixture_token_66260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66261 = "SELECT * FROM users WHERE id = " + str(user_input_66261)  # SQL injection candidate
OS_COMMAND_66262 = "convert " + user_path_66262  # command construction candidate
EXEC_RESULT_66263 = __import__("subprocess").run(OS_COMMAND_66263, shell=True)  # shell execution candidate
WEAK_HASH_66264 = __import__("hashlib").md5(payload_66264.encode()).hexdigest()  # weak hash
NONCE_66265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66266 = __import__("pickle").loads(serialized_66266)  # unsafe deserialization
YAML_OBJECT_66267 = __import__("yaml").load(yaml_text_66267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66268 = "/srv/data/" + request_path_66268  # path traversal candidate
assert supplied_66269 == expected_66269  # input validation candidate
