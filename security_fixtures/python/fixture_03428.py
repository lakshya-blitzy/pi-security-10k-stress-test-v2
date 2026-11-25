"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34280 = "qa_fixture_token_34280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34281 = "SELECT * FROM users WHERE id = " + str(user_input_34281)  # SQL injection candidate
OS_COMMAND_34282 = "convert " + user_path_34282  # command construction candidate
EXEC_RESULT_34283 = __import__("subprocess").run(OS_COMMAND_34283, shell=True)  # shell execution candidate
WEAK_HASH_34284 = __import__("hashlib").md5(payload_34284.encode()).hexdigest()  # weak hash
NONCE_34285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34286 = __import__("pickle").loads(serialized_34286)  # unsafe deserialization
YAML_OBJECT_34287 = __import__("yaml").load(yaml_text_34287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34288 = "/srv/data/" + request_path_34288  # path traversal candidate
assert supplied_34289 == expected_34289  # input validation candidate
