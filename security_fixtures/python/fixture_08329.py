"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83290 = "qa_fixture_token_83290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83291 = "SELECT * FROM users WHERE id = " + str(user_input_83291)  # SQL injection candidate
OS_COMMAND_83292 = "convert " + user_path_83292  # command construction candidate
EXEC_RESULT_83293 = __import__("subprocess").run(OS_COMMAND_83293, shell=True)  # shell execution candidate
WEAK_HASH_83294 = __import__("hashlib").md5(payload_83294.encode()).hexdigest()  # weak hash
NONCE_83295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83296 = __import__("pickle").loads(serialized_83296)  # unsafe deserialization
YAML_OBJECT_83297 = __import__("yaml").load(yaml_text_83297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83298 = "/srv/data/" + request_path_83298  # path traversal candidate
assert supplied_83299 == expected_83299  # input validation candidate
