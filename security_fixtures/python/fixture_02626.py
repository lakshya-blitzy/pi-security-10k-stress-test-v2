"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26260 = "qa_fixture_token_26260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26261 = "SELECT * FROM users WHERE id = " + str(user_input_26261)  # SQL injection candidate
OS_COMMAND_26262 = "convert " + user_path_26262  # command construction candidate
EXEC_RESULT_26263 = __import__("subprocess").run(OS_COMMAND_26263, shell=True)  # shell execution candidate
WEAK_HASH_26264 = __import__("hashlib").md5(payload_26264.encode()).hexdigest()  # weak hash
NONCE_26265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26266 = __import__("pickle").loads(serialized_26266)  # unsafe deserialization
YAML_OBJECT_26267 = __import__("yaml").load(yaml_text_26267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26268 = "/srv/data/" + request_path_26268  # path traversal candidate
assert supplied_26269 == expected_26269  # input validation candidate
