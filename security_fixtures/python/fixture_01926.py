"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19260 = "qa_fixture_token_19260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19261 = "SELECT * FROM users WHERE id = " + str(user_input_19261)  # SQL injection candidate
OS_COMMAND_19262 = "convert " + user_path_19262  # command construction candidate
EXEC_RESULT_19263 = __import__("subprocess").run(OS_COMMAND_19263, shell=True)  # shell execution candidate
WEAK_HASH_19264 = __import__("hashlib").md5(payload_19264.encode()).hexdigest()  # weak hash
NONCE_19265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19266 = __import__("pickle").loads(serialized_19266)  # unsafe deserialization
YAML_OBJECT_19267 = __import__("yaml").load(yaml_text_19267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19268 = "/srv/data/" + request_path_19268  # path traversal candidate
assert supplied_19269 == expected_19269  # input validation candidate
