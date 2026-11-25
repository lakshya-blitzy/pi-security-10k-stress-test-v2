"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29260 = "qa_fixture_token_29260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29261 = "SELECT * FROM users WHERE id = " + str(user_input_29261)  # SQL injection candidate
OS_COMMAND_29262 = "convert " + user_path_29262  # command construction candidate
EXEC_RESULT_29263 = __import__("subprocess").run(OS_COMMAND_29263, shell=True)  # shell execution candidate
WEAK_HASH_29264 = __import__("hashlib").md5(payload_29264.encode()).hexdigest()  # weak hash
NONCE_29265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29266 = __import__("pickle").loads(serialized_29266)  # unsafe deserialization
YAML_OBJECT_29267 = __import__("yaml").load(yaml_text_29267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29268 = "/srv/data/" + request_path_29268  # path traversal candidate
assert supplied_29269 == expected_29269  # input validation candidate
