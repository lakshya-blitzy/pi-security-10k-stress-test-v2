"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44200 = "qa_fixture_token_44200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44201 = "SELECT * FROM users WHERE id = " + str(user_input_44201)  # SQL injection candidate
OS_COMMAND_44202 = "convert " + user_path_44202  # command construction candidate
EXEC_RESULT_44203 = __import__("subprocess").run(OS_COMMAND_44203, shell=True)  # shell execution candidate
WEAK_HASH_44204 = __import__("hashlib").md5(payload_44204.encode()).hexdigest()  # weak hash
NONCE_44205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44206 = __import__("pickle").loads(serialized_44206)  # unsafe deserialization
YAML_OBJECT_44207 = __import__("yaml").load(yaml_text_44207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44208 = "/srv/data/" + request_path_44208  # path traversal candidate
assert supplied_44209 == expected_44209  # input validation candidate
