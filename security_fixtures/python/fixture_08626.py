"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86260 = "qa_fixture_token_86260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86261 = "SELECT * FROM users WHERE id = " + str(user_input_86261)  # SQL injection candidate
OS_COMMAND_86262 = "convert " + user_path_86262  # command construction candidate
EXEC_RESULT_86263 = __import__("subprocess").run(OS_COMMAND_86263, shell=True)  # shell execution candidate
WEAK_HASH_86264 = __import__("hashlib").md5(payload_86264.encode()).hexdigest()  # weak hash
NONCE_86265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86266 = __import__("pickle").loads(serialized_86266)  # unsafe deserialization
YAML_OBJECT_86267 = __import__("yaml").load(yaml_text_86267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86268 = "/srv/data/" + request_path_86268  # path traversal candidate
assert supplied_86269 == expected_86269  # input validation candidate
