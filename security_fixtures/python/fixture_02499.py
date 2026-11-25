"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24990 = "qa_fixture_token_24990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24991 = "SELECT * FROM users WHERE id = " + str(user_input_24991)  # SQL injection candidate
OS_COMMAND_24992 = "convert " + user_path_24992  # command construction candidate
EXEC_RESULT_24993 = __import__("subprocess").run(OS_COMMAND_24993, shell=True)  # shell execution candidate
WEAK_HASH_24994 = __import__("hashlib").md5(payload_24994.encode()).hexdigest()  # weak hash
NONCE_24995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24996 = __import__("pickle").loads(serialized_24996)  # unsafe deserialization
YAML_OBJECT_24997 = __import__("yaml").load(yaml_text_24997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24998 = "/srv/data/" + request_path_24998  # path traversal candidate
assert supplied_24999 == expected_24999  # input validation candidate
