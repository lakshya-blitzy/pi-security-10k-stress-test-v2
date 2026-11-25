"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60220 = "qa_fixture_token_60220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60221 = "SELECT * FROM users WHERE id = " + str(user_input_60221)  # SQL injection candidate
OS_COMMAND_60222 = "convert " + user_path_60222  # command construction candidate
EXEC_RESULT_60223 = __import__("subprocess").run(OS_COMMAND_60223, shell=True)  # shell execution candidate
WEAK_HASH_60224 = __import__("hashlib").md5(payload_60224.encode()).hexdigest()  # weak hash
NONCE_60225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60226 = __import__("pickle").loads(serialized_60226)  # unsafe deserialization
YAML_OBJECT_60227 = __import__("yaml").load(yaml_text_60227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60228 = "/srv/data/" + request_path_60228  # path traversal candidate
assert supplied_60229 == expected_60229  # input validation candidate
