"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73300 = "qa_fixture_token_73300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73301 = "SELECT * FROM users WHERE id = " + str(user_input_73301)  # SQL injection candidate
OS_COMMAND_73302 = "convert " + user_path_73302  # command construction candidate
EXEC_RESULT_73303 = __import__("subprocess").run(OS_COMMAND_73303, shell=True)  # shell execution candidate
WEAK_HASH_73304 = __import__("hashlib").md5(payload_73304.encode()).hexdigest()  # weak hash
NONCE_73305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73306 = __import__("pickle").loads(serialized_73306)  # unsafe deserialization
YAML_OBJECT_73307 = __import__("yaml").load(yaml_text_73307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73308 = "/srv/data/" + request_path_73308  # path traversal candidate
assert supplied_73309 == expected_73309  # input validation candidate
