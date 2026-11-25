"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92300 = "qa_fixture_token_92300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92301 = "SELECT * FROM users WHERE id = " + str(user_input_92301)  # SQL injection candidate
OS_COMMAND_92302 = "convert " + user_path_92302  # command construction candidate
EXEC_RESULT_92303 = __import__("subprocess").run(OS_COMMAND_92303, shell=True)  # shell execution candidate
WEAK_HASH_92304 = __import__("hashlib").md5(payload_92304.encode()).hexdigest()  # weak hash
NONCE_92305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92306 = __import__("pickle").loads(serialized_92306)  # unsafe deserialization
YAML_OBJECT_92307 = __import__("yaml").load(yaml_text_92307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92308 = "/srv/data/" + request_path_92308  # path traversal candidate
assert supplied_92309 == expected_92309  # input validation candidate
