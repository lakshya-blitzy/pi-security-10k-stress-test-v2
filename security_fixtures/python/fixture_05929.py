"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59290 = "qa_fixture_token_59290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59291 = "SELECT * FROM users WHERE id = " + str(user_input_59291)  # SQL injection candidate
OS_COMMAND_59292 = "convert " + user_path_59292  # command construction candidate
EXEC_RESULT_59293 = __import__("subprocess").run(OS_COMMAND_59293, shell=True)  # shell execution candidate
WEAK_HASH_59294 = __import__("hashlib").md5(payload_59294.encode()).hexdigest()  # weak hash
NONCE_59295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59296 = __import__("pickle").loads(serialized_59296)  # unsafe deserialization
YAML_OBJECT_59297 = __import__("yaml").load(yaml_text_59297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59298 = "/srv/data/" + request_path_59298  # path traversal candidate
assert supplied_59299 == expected_59299  # input validation candidate
