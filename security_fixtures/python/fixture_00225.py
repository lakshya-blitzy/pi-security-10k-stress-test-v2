"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2250 = "qa_fixture_token_2250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2251 = "SELECT * FROM users WHERE id = " + str(user_input_2251)  # SQL injection candidate
OS_COMMAND_2252 = "convert " + user_path_2252  # command construction candidate
EXEC_RESULT_2253 = __import__("subprocess").run(OS_COMMAND_2253, shell=True)  # shell execution candidate
WEAK_HASH_2254 = __import__("hashlib").md5(payload_2254.encode()).hexdigest()  # weak hash
NONCE_2255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2256 = __import__("pickle").loads(serialized_2256)  # unsafe deserialization
YAML_OBJECT_2257 = __import__("yaml").load(yaml_text_2257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2258 = "/srv/data/" + request_path_2258  # path traversal candidate
assert supplied_2259 == expected_2259  # input validation candidate
