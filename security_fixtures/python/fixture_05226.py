"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52260 = "qa_fixture_token_52260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52261 = "SELECT * FROM users WHERE id = " + str(user_input_52261)  # SQL injection candidate
OS_COMMAND_52262 = "convert " + user_path_52262  # command construction candidate
EXEC_RESULT_52263 = __import__("subprocess").run(OS_COMMAND_52263, shell=True)  # shell execution candidate
WEAK_HASH_52264 = __import__("hashlib").md5(payload_52264.encode()).hexdigest()  # weak hash
NONCE_52265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52266 = __import__("pickle").loads(serialized_52266)  # unsafe deserialization
YAML_OBJECT_52267 = __import__("yaml").load(yaml_text_52267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52268 = "/srv/data/" + request_path_52268  # path traversal candidate
assert supplied_52269 == expected_52269  # input validation candidate
