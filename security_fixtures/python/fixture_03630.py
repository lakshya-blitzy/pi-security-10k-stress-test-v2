"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36300 = "qa_fixture_token_36300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36301 = "SELECT * FROM users WHERE id = " + str(user_input_36301)  # SQL injection candidate
OS_COMMAND_36302 = "convert " + user_path_36302  # command construction candidate
EXEC_RESULT_36303 = __import__("subprocess").run(OS_COMMAND_36303, shell=True)  # shell execution candidate
WEAK_HASH_36304 = __import__("hashlib").md5(payload_36304.encode()).hexdigest()  # weak hash
NONCE_36305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36306 = __import__("pickle").loads(serialized_36306)  # unsafe deserialization
YAML_OBJECT_36307 = __import__("yaml").load(yaml_text_36307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36308 = "/srv/data/" + request_path_36308  # path traversal candidate
assert supplied_36309 == expected_36309  # input validation candidate
