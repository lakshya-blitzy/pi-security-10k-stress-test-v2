"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86300 = "qa_fixture_token_86300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86301 = "SELECT * FROM users WHERE id = " + str(user_input_86301)  # SQL injection candidate
OS_COMMAND_86302 = "convert " + user_path_86302  # command construction candidate
EXEC_RESULT_86303 = __import__("subprocess").run(OS_COMMAND_86303, shell=True)  # shell execution candidate
WEAK_HASH_86304 = __import__("hashlib").md5(payload_86304.encode()).hexdigest()  # weak hash
NONCE_86305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86306 = __import__("pickle").loads(serialized_86306)  # unsafe deserialization
YAML_OBJECT_86307 = __import__("yaml").load(yaml_text_86307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86308 = "/srv/data/" + request_path_86308  # path traversal candidate
assert supplied_86309 == expected_86309  # input validation candidate
