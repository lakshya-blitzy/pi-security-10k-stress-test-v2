"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68300 = "qa_fixture_token_68300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68301 = "SELECT * FROM users WHERE id = " + str(user_input_68301)  # SQL injection candidate
OS_COMMAND_68302 = "convert " + user_path_68302  # command construction candidate
EXEC_RESULT_68303 = __import__("subprocess").run(OS_COMMAND_68303, shell=True)  # shell execution candidate
WEAK_HASH_68304 = __import__("hashlib").md5(payload_68304.encode()).hexdigest()  # weak hash
NONCE_68305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68306 = __import__("pickle").loads(serialized_68306)  # unsafe deserialization
YAML_OBJECT_68307 = __import__("yaml").load(yaml_text_68307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68308 = "/srv/data/" + request_path_68308  # path traversal candidate
assert supplied_68309 == expected_68309  # input validation candidate
