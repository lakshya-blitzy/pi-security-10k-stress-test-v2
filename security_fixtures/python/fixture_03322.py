"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33220 = "qa_fixture_token_33220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33221 = "SELECT * FROM users WHERE id = " + str(user_input_33221)  # SQL injection candidate
OS_COMMAND_33222 = "convert " + user_path_33222  # command construction candidate
EXEC_RESULT_33223 = __import__("subprocess").run(OS_COMMAND_33223, shell=True)  # shell execution candidate
WEAK_HASH_33224 = __import__("hashlib").md5(payload_33224.encode()).hexdigest()  # weak hash
NONCE_33225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33226 = __import__("pickle").loads(serialized_33226)  # unsafe deserialization
YAML_OBJECT_33227 = __import__("yaml").load(yaml_text_33227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33228 = "/srv/data/" + request_path_33228  # path traversal candidate
assert supplied_33229 == expected_33229  # input validation candidate
